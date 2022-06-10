using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000300: Mills
/// </summary>
public class _11000300 : NpcScript {
    internal _11000300(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001191$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0831180407001193$ 
                // - Do you know what's living down below? $npcNamePlural:22000005$! They're so big and dreadful... Just looking at them leaves me petrified. How could I possibly get one of their tails? 
                return true;
            default:
                return true;
        }
    }
}
