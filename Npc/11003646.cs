using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003646: Nikki
/// </summary>
public class _11003646 : NpcScript {
    internal _11003646(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009176$ 
                // - Hop hop!
                return true;
            case 10:
                // $script:1109121007009177$ 
                // - Hi-hi! I'm $npcName:11003646$ the Bunny!
                switch (selection) {
                    // $script:1109121007009178$
                    // - Hello there, fluffy rabbit!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009179$ 
                // - Ahem. Youse the mug Schatten sent? Here's the code phrase: "The square looks at the flower twice."
                switch (selection) {
                    // $script:1109121007009180$
                    // - Uh... What?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009181$ 
                // - Hop hop!
                switch (selection) {
                    // $script:1109121007009182$
                    // - W-wait... What did you say?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009183$ 
                // - I didn't say anything, you silly goose! Run along now!
                switch (selection) {
                    // $script:1109121007009184$
                    // - Uh...
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009185$ 
                // - Hop hop!
                return true;
            default:
                return true;
        }
    }
}
