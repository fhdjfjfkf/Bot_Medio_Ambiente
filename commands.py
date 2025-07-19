import discord
from discord.ext import commands

reciclables = {
    "botella": "se recicla en el contenedor amarillo",
    "metal": "se recicla en el contenedor amarillo",
    "cajas": "se recicla en el contenedor azul",
    "vidrio": "se recicla en el contenedor verde",
    "desechos": "se recicla en el contenedor negro",
    "cascaras de frutas": "se recicla en el contenedor marrón",
    "tapas plásticas": "se recicla en el contenedor amarillo",
    "papel": "se recicla en el contenedor azul",
    "cartón": "se recicla en el contenedor azul",
    "lata": "se recicla en el contenedor amarillo",
    "brik": "se recicla en el contenedor amarillo",
    "ropa": "no va al tacho, se dona o va al punto limpio",
    "pilas": "no va al tacho, se lleva a un punto limpio especial",
    "juguete roto": "va al contenedor negro o punto limpio",
    "madera tratada": "no se recicla, llevar a un punto limpio",
    "papel aluminio": "se recicla en el contenedor amarillo (si está limpio)",
    "revistas": "se recicla en el contenedor azul",
    "periódico": "se recicla en el contenedor azul",
    "botella de vidrio": "se recicla en el contenedor verde",
    "tetrapak": "se recicla en el contenedor amarillo",
    "bolsa plástica": "se recicla en el contenedor amarillo (si está limpia)",
    "bandeja de aluminio": "se recicla en el contenedor amarillo (si está limpia)",
    "cds/dvds": "no se reciclan en casa, llévalos a un punto limpio",
    "focos": "no van al tacho, punto limpio especial",
    "termómetros": "no van al tacho, residuos peligrosos",
    "aserrín": "se puede compostar si es natural (contenedor marrón)",
    "cepillo de dientes": "contenedor negro o punto limpio",
    "pañuelo de papel usado": "contenedor negro",
    "latas de conserva": "se reciclan en el contenedor amarillo",
    "tetrabrik": "se recicla en el contenedor amarillo"
}

contenedores = {
    "amarillo": ["botellas", "metales", "plásticos", "tetrapak", "latas", "brik", "bandejas de aluminio", "papel aluminio (limpio)"],
    "azul": ["papel", "cartón", "revistas", "periódicos"],
    "verde": ["vidrio", "botellas de vidrio"],
    "marrón": ["restos orgánicos", "cáscaras de frutas", "aserrín natural"],
    "negro": ["desechos no reciclables", "pañuelos usados", "cepillos de dientes", "juguetes rotos"],
    "punto limpio": ["pilas", "ropa", "cds/dvds", "focos", "termómetros", "madera tratada"]
}

def setup(bot):
    @bot.command(name="reciclables")
    async def reciclables_cmd(ctx, *args):
        if not args:
            await ctx.send("❗ Por favor, escribe el nombre del objeto que quieres consultar.")
            return

        entrada = ' '.join(args).lower()
        encontrado = False

        for item, descripcion in reciclables.items():
            if entrada in item.lower():
                embed = discord.Embed(
                    title="♻️ Información de reciclaje",
                    description=f"**Objeto:** {item.capitalize()}",
                    color=0x00b050
                )
                embed.add_field(name="¿Dónde se recicla?", value=descripcion, inline=False)
                embed.set_footer(text="Consulta de reciclaje • Navia Bot")
                await ctx.send(embed=embed)
                encontrado = True
                break

        if not encontrado:
            embed = discord.Embed(
                title="❌ Objeto no encontrado",
                description="No encontré ese objeto en la lista. Intenta con otro nombre o revisa la ortografía.",
                color=0xcc0000
            )
            await ctx.send(embed=embed)

    @bot.command(name="lista_reciclables")
    async def lista_reciclables(ctx):
        lista = ', '.join(sorted(reciclables.keys()))
        embed = discord.Embed(
            title="🗂️ Lista de objetos reconocidos",
            description=lista,
            color=0x0099ff
        )
        await ctx.send(embed=embed)

    @bot.command(name="contenedor")
    async def contenedor_info(ctx, color: str):
        color = color.lower()
        if color in contenedores:
            items = ', '.join(contenedores[color])
            embed = discord.Embed(
                title=f"🗑️ ¿Qué va en el contenedor {color}?",
                description=items.capitalize(),
                color=0xf4b400 if color == "amarillo" else 0x4285f4 if color == "azul" else 0x34a853 if color == "verde" else 0x8d6e63 if color == "marrón" else 0x333333
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("❗ Color de contenedor no reconocido. Intenta con: amarillo, azul, verde, marrón, negro o punto limpio.")
