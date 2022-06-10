using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004478: Hani
/// </summary>
public class _11004478 : NpcScript {
    internal _11004478(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228141007012420$ 
                // - Blake is so... bedazzling! Don't you think so, too?
                return true;
            case 10:
                // $script:1228141007012421$ 
                // - Blake is so... bedazzling! Don't you think so, too?
                switch (selection) {
                    // $script:1228141007012422$
                    // - Bedazzling. Sure. Let's say yes.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1228141007012423$ 
                // - It's like we're witnessing history. The day Blake set foot in the new world!
                // $script:1228141007012424$ 
                // - Wanna join the new Blake Fan Club—Kritias Branch? I've got the paperwork right here!
                switch (selection) {
                    // $script:1228141007012425$
                    // - Oh no, something urgent just came up. Bye.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1228141007012426$ 
                // - Really? Shoot... Well, come back soon, before we fill up!
                return true;
            default:
                return true;
        }
    }
}
