// Acceso privado al sitio del Proyecto Panadería Córdoba (lógica en panaderia_cordoba/site/middleware.js).
import handler from './panaderia_cordoba/site/middleware.js';

export const config = { matcher: '/:path*' };
export default handler;
