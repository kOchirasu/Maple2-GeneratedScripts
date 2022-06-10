using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000491: Cathy Catalina
/// </summary>
public class _11000491 : NpcScript {
    internal _11000491(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;70;80
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002150$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0831180407002153$ 
                // - Right now, Goldus Group is the biggest company in $map:02000100$, but that'll soon change. I'll be crushing $npcName:11000252[gender:0]$ under my heel before you know it. 
                return true;
            case 40:
                // $script:0831180407002154$ 
                // - What? You want to know if I'm single? 
                // $script:0831180407002155$ 
                // - Hah! I don't need a man. All men are narcissistic, chauvinist pigs. I hate them! 
                return true;
            case 70:
                // $script:0831180407002156$ 
                // - Can't you see I'm busy? If it's not urgent, then scram. 
                return true;
            case 80:
                // $script:0831180407002157$ 
                // - I don't sell anything on credit. I trust money more than I trust people. 
                return true;
            default:
                return true;
        }
    }
}
