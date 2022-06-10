using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003159: Beuti
/// </summary>
public class _11003159 : NpcScript {
    internal _11003159(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008059$ 
                // - What is it?
                return true;
            case 30:
                // $script:0306155707008062$ 
                // - I filled my backpack with flowers, and now I can smell them all the time! Oh, don't worry. They're not heavy at all.
                return true;
            default:
                return true;
        }
    }
}
