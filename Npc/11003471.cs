using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003471: 
/// </summary>
public class _11003471 : NpcScript {
    internal _11003471(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817152010001894$ 
                // - Greetings. 
                switch (selection) {
                    // $script:0829173610001911$
                    // - I want to go to $map:63000057$.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0829173610001913$
                    // - I want to look at my daily rewards.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0817152010001901$ functionID=1 
                // - No problem, no problem! I'll send it to you right away. Have a great time! 
                return true;
            case 32:
                // $script:0817152010001902$ functionID=1 
                // - Looking for some fun at $map:02000405$? Then off you go! 
                return true;
            case 33:
                // $script:0817152010001903$ functionID=1 
                // - I give you all these things because I care so dang much! 
                return true;
            default:
                return true;
        }
    }
}
