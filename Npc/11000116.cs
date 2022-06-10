using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000116: Anthony
/// </summary>
public class _11000116 : NpcScript {
    internal _11000116(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000490$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000493$ 
                // - $MyPCName$, do you think this is just a simple earthquake?
                switch (selection) {
                    // $script:0831180407000494$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000495$
                    // - Seems unlikely.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000496$ functionID=1 
                // - ...
                // $script:0831180407000497$ 
                // - All right. Fine. Just keep thinking that way.
                return true;
            case 32:
                // $script:0831180407000498$ 
                // - I don't have proof yet, but I'm certain this wasn't a simple earthquake. I suspect a massive shadow gate has opened somewhere, causing this upheaval.
                switch (selection) {
                    // $script:0831180407000499$
                    // - What is a shadow gate?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407000500$ 
                // - You've never seen a shadow gate? Lucky you. They're doorways to the Land of Darkness. The empress herself has forbidden anyone from using such gates.
                // $script:0831180407000501$ 
                // - Our forces have the Shadow Gate blockaded and guarded to ensure nothing escapes. There are rumored to be unguarded passages hidden around Maple World, and some shady types use those to pass through to the Land of Darkness.
                // $script:0831180407000502$ 
                // - I was told that those who dare enter the Land of Darkness would have both their bodies and souls devoured by demons. However, that sounds like something made up to keep people from exploring. My plan is to find a shadow gate and travel to the Land of Darkness myself, so don't tell anyone.
                return true;
            default:
                return true;
        }
    }
}
