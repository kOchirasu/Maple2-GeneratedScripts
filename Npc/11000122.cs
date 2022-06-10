using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000122: Gregory
/// </summary>
public class _11000122 : NpcScript {
    internal _11000122(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000527$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000529$ 
                // - I see you're curious about $itemPlural:20000016$. Well... After the Blue Lapenta was destroyed, hundreds of Defenders fell to the shadow toxin that spread from the Land of Darkness.
                // $script:0831180407000530$ 
                // - I tried everything reagent I could get my hands on to cure it, and the one that did it was the $item:20000045$, growing right here at the $map:02000146$. It took time to perfect the compounding process, but now my $itemPlural:20000016$ are key to the struggle against the darkness.
                return true;
            default:
                return true;
        }
    }
}
