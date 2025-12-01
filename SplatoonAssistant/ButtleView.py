import random
import discord
from discord.ui import View, Button


# 勝利判定を定義する View クラス
class ButtleView(View):


    def __init__(self, members, start_time, count, embed):
        super().__init__(timeout=900)

        self.members = members
        self.start_time = start_time
        self.count = count

        embed.title = "⚔️ 試合中..."
        embed.color = discord.Color.purple()
        embed.set_footer(text=f"勝利チームはどちらですか？")
        self.init_view = embed


    # 「アルファチーム」ボタンの定義
    @discord.ui.button(label="アルファチーム", style=discord.ButtonStyle.primary, emoji="🟨")
    async def alpha_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        caution_view = CautionView(self.members, self.start_time, self.count, self.init_view, "🟨 アルファチーム")
        await interaction.edit_original_response(
            embed=caution_view.init_embed,
            view=caution_view
        )

        
    # 「ブラボーチーム」ボタンの定義
    @discord.ui.button(label="ブラボーチーム", style=discord.ButtonStyle.primary, emoji="🟦")
    async def beta_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        caution_view = CautionView(self.members, self.start_time, self.count, self.init_view, "🟦 ブラボーチーム")
        await interaction.edit_original_response(
            embed=caution_view.init_embed,
            view=caution_view
        )


    # 「無効試合」ボタンの定義
    @discord.ui.button(label="無効試合", style=discord.ButtonStyle.secondary, emoji="❌")
    async def invalid_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        caution_view = CautionView(self.members, self.start_time, self.count, self.init_view, None)
        await interaction.edit_original_response(
            embed=caution_view.init_embed,
            view=caution_view
        )

        
# 最終確認を定義する View クラス
class CautionView(View):


    def __init__(self, members, start_time, count, embed, winner):
        super().__init__(timeout=900)

        self.members = members
        self.start_time = start_time
        self.count = count
        self.embed = embed
        self.winner = winner

        info = winner if winner is not None else "❌ 無効試合"
        self.init_embed = discord.Embed(
            title="⚠️ 確認",
            description=f"{info} で間違いないですか？",
            color=discord.Color.red()
        )


    # 「いいえ」ボタンの定義
    @discord.ui.button(label="いいえ", style=discord.ButtonStyle.danger)
    async def cancel_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        buttle_view = ButtleView(self.members, self.start_time, self.count, self.embed)
        await interaction.edit_original_response(
            embed=buttle_view.init_view,
            view=buttle_view
        )


    # 「はい」ボタンの定義
    @discord.ui.button(label="はい", style=discord.ButtonStyle.success)
    async def confirm_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        from TeamControlView import TeamControlView
        if self.winner is not None:
            self.count += 1
        team_view = TeamControlView(self.members, self.start_time, self.count)
        await interaction.edit_original_response(
            embed=team_view.current_embed,
            view=team_view
        )