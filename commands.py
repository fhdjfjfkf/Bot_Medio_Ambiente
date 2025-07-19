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
                    color=0x00b050  # Verde
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
                color=0xcc0000  # Rojo
            )
            await ctx.send(embed=embed)
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
