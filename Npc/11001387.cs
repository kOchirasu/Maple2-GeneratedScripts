using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001387: Krata
/// </summary>
public class _11001387 : NpcScript {
    internal _11001387(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005387$ 
                // - I'm tired. Really tired!
                return true;
            case 40:
                // $script:1223165107005549$ 
                // - I've been getting terrible joint pain lately. Normally that'd mean there's a storm brewing, but it doesn't rain here. Very strange.
                // $script:1223165107005550$ 
                // - There's a rumor that all the ailments that have struck the town lately are from an ancient curse.
                switch (selection) {
                    // $script:1223165107005551$
                    // - What kind of curse?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1223165107005552$ 
                // - Never mind. I shouldn't have mentioned it to an outsider in the first place. If you'll excuse me, I need to gather herbs for my arthritis.
                return true;
            default:
                return true;
        }
    }
}
