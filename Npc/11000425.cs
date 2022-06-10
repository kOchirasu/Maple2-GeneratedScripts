using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000425: Loki
/// </summary>
public class _11000425 : NpcScript {
    internal _11000425(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001772$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407001774$ 
                // - These vultures are not tamed. What if they fly me to some unfamiliar place or drop me in midair?
                return true;
            default:
                return true;
        }
    }
}
