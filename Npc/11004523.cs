using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004523: Corny Soldieretto
/// </summary>
public class _11004523 : NpcScript {
    internal _11004523(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012500$ 
                // - Beeep... Beeep...
                return true;
            case 10:
                // $script:0103163407012501$ 
                // - Mathematical query: why was six afraid of seven?
                // $script:0103163407012502$ 
                // - Answer: because seven ate nine. Ha! Ha! Ha! Ha!
                return true;
            default:
                return true;
        }
    }
}
