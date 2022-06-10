using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003514: Havika
/// </summary>
public class _11003514 : NpcScript {
    internal _11003514(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008814$ 
                // - What's going on?
                return true;
            case 30:
                // $script:0817044507008817$ 
                // - What's going on...?
                switch (selection) {
                    // $script:0817044507008818$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008819$ 
                // - The singewings live on Bahram Mountain to the north. They protect their eggs on the mountaintop. You can get Blazing Courage by stealing those eggs...
                switch (selection) {
                    // $script:0817044507008820$
                    // - Tell me about Bahram Mountain.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0817044507008821$
                    // - Tell me about the singewings.
                    case 1:
                        Id = 33;
                        return false;
                    // $script:0817044507008822$
                    // - Tell me about the dragon eggs.
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            case 32:
                // $script:0817044507008823$ 
                // - It's actually a burning volcano. I wouldn't climb it without the right gear. Unless you're lava resistant...? 
                switch (selection) {
                    // $script:0817044507008824$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 33:
                // $script:0817044507008825$ 
                // - The singewings are fire-breathers. Their breath is even hotter than lava... 
                switch (selection) {
                    // $script:0817133807008875$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 34:
                // $script:0817044507008826$ 
                // - Dragon eggs don't tend to wander off on their own. What the singewings will do when they notice their eggs are missing... I can't say. 
                switch (selection) {
                    // $script:0817133807008876$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0817044507008827$ 
                // - Do you have more questions?
                switch (selection) {
                    // $script:0817044507008828$
                    // - Tell me about Bahram Mountain.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0817044507008829$
                    // - Tell me about the singewings.
                    case 1:
                        Id = 33;
                        return false;
                    // $script:0817044507008830$
                    // - Tell me about the dragon eggs.
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
