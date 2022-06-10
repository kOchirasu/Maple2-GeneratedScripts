using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000039: Namid
/// </summary>
public class _11000039 : NpcScript {
    internal _11000039(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000204$ 
                // - Who will protect $map:02000051$?
                return true;
            case 40:
                // $script:0831180407000208$ 
                // - Sometimes you get what you want. Sometimes you must settle.
                return true;
            default:
                return true;
        }
    }
}
