using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001073: Wild Feet
/// </summary>
public class _11001073 : NpcScript {
    internal _11001073(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003659$ 
                // - Toh! Toh! Toh!
                return true;
            case 30:
                // $script:0831180407003662$ 
                // - I don't talk to those who do not practice martial arts.
                return true;
            default:
                return true;
        }
    }
}
