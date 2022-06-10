using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000529: Blackeye
/// </summary>
public class _11000529 : NpcScript {
    internal _11000529(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002267$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0831180407002270$ 
                // - Dark Wind has changed too much. Now it's crushing the citizens under authoritarian rule instead of protecting them like they used to. I can't let this continue.
                return true;
            case 40:
                // $script:0831180407002271$ 
                // - $MyPCName$, do the people in this city look happy to you?
                switch (selection) {
                    // $script:0831180407002272$
                    // - Yep!
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002273$
                    // - Beats me.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002274$ 
                // - Then you're a fool. There's no point in discussing this further. Leave.
                return true;
            case 42:
                // $script:0831180407002275$ 
                // - Try to see through their deceptions. It's not hard to find the rotting heart of this city.
                return true;
            default:
                return true;
        }
    }
}
