using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004185: Monshel
/// </summary>
public class _11004185 : NpcScript {
    internal _11004185(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010632$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:0806025707010633$ 
                // - To reclaim all I have lost, I must find a champion in the greatest of games! 
                return true;
            default:
                return true;
        }
    }
}
