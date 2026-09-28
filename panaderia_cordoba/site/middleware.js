// Acceso privado al sitio: cada socio entra con su usuario y contraseña.
// Corre en Vercel (Routing Middleware) antes de servir cualquier página o archivo.
import { next } from '@vercel/functions';
import fileUsers from './auth_users.js';

export const config = { matcher: '/:path*' };

const REALM = 'Basic realm="Proyecto PAN-CBA - acceso de socios", charset="UTF-8"';

function users() {
  // Permite reemplazar los usuarios desde una variable de entorno sin tocar el repo.
  try { if (process.env.SITE_USERS) return JSON.parse(process.env.SITE_USERS); } catch (e) { /* usa el archivo */ }
  return fileUsers;
}

async function sha256hex(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

function safeEqual(a, b) {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

function denied(msg = 'Acceso restringido a los socios del proyecto.') {
  return new Response(msg, { status: 401, headers: { 'WWW-Authenticate': REALM, 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' } });
}

export default async function middleware(request) {
  const url = new URL(request.url);
  if (url.pathname === '/salir') return denied('Sesión cerrada. Cerrá esta pestaña o volvé a ingresar con otro usuario.');

  const auth = request.headers.get('authorization') || '';
  if (!auth.startsWith('Basic ')) return denied();
  let decoded = '';
  try { decoded = new TextDecoder().decode(Uint8Array.from(atob(auth.slice(6)), (c) => c.charCodeAt(0))); } catch (e) { return denied(); }
  const i = decoded.indexOf(':');
  if (i < 0) return denied();
  const user = decoded.slice(0, i).trim().toLowerCase();
  const pass = decoded.slice(i + 1);
  const u = users()[user];
  if (!u || !safeEqual(await sha256hex(u.salt + pass), u.hash)) return denied();

  return next({
    headers: {
      'Set-Cookie': `socio=${u.id}; Path=/; Secure; SameSite=Lax; Max-Age=2592000`,
      'Cache-Control': 'private, no-store',
      'X-Robots-Tag': 'noindex, nofollow',
    },
  });
}
