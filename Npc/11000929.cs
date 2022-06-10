using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000929: JJ Tutor
/// </summary>
public class _11000929 : NpcScript {
    internal _11000929(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003298$ 
                // - How did you find this place?!
                return true;
            case 30:
                // $script:0831180407003301$ 
                // - The saga of a thousand-year-old turtle writer. That's got to be a story worth telling!
                return true;
            default:
                return true;
        }
    }
}
