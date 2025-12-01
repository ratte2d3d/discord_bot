import discord
from discord.ui import View, UserSelect
from TeamControlView import TeamControlView


# ユーザー選択メニューを定義する View クラス
class MemberSelectView(View):


    # タイムアウト時間など、Viewの基本設定をここに書く
    def __init__(self, start_time, count=1):
        super().__init__(timeout=180)

        # 日付と試合回数
        self.start_time = start_time
        self.count = count
        # Embedの作成
        self.init_embed = discord.Embed(
            title="👥 メンバー選択",
            description="▼ 参加メンバーを以下から選択してください",
            color=discord.Color.blurple()
        )


    # ユーザー選択メニュー（UserSelect）をViewに追加
    @discord.ui.select(
        cls=UserSelect,
        placeholder="メンバー選択",
        min_values=2,
        max_values=10
    )
    async def select_callback(self, interaction: discord.Interaction, select: UserSelect):
        # 選択完了時の処理
        selected_members = select.values
        team_view = TeamControlView(selected_members, self.start_time, self.count)
        await interaction.response.edit_message(
            embed=team_view.current_embed,
            view=team_view
        )