#!/usr/bin/env python3
"""Genera (o regenera) usuarios y contraseñas del sitio.

Uso:
  python crear_usuarios.py            → crea contraseñas nuevas para TODOS los socios
  python crear_usuarios.py laura      → regenera sólo la de 'laura'

Imprime las contraseñas UNA sola vez (no se guardan en el repo) y escribe auth_users.js
con el hash salado de cada una. Luego hay que hacer commit + push de auth_users.js.
"""
import hashlib, json, os, re, secrets, sys

SITE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(SITE, "config.json"), encoding="utf-8"))
OUT = os.path.join(SITE, "auth_users.js")
ALPH = "abcdefghjkmnpqrstuvwxyz23456789"  # sin caracteres confusos (l/1, o/0)


def load_existing():
    if not os.path.exists(OUT):
        return {}
    m = re.search(r"export default (\{.*\});", open(OUT, encoding="utf-8").read(), re.S)
    return json.loads(m.group(1)) if m else {}


def new_password():
    return "-".join("".join(secrets.choice(ALPH) for _ in range(4)) for _ in range(4))


def main():
    only = set(sys.argv[1:])
    users = load_existing()
    for s in CFG["socios"]:
        user = s["usuario"]
        if only and user not in only:
            continue
        pw = new_password()
        salt = secrets.token_hex(16)
        users[user] = {"id": s["id"], "nombre": s["nombre"], "salt": salt,
                       "hash": hashlib.sha256((salt + pw).encode()).hexdigest()}
        print(f"{s['nombre']:<26} usuario: {user:<12} contraseña: {pw}")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Generado por crear_usuarios.py — sólo contiene hashes salados, nunca contraseñas.\n")
        f.write("export default " + json.dumps(users, ensure_ascii=False, indent=2) + ";\n")
    print(f"\nActualizado {OUT}. Hacer commit + push para que tome efecto.")


if __name__ == "__main__":
    main()
