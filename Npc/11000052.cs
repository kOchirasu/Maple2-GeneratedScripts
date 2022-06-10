using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000052: Varlos
/// </summary>
public class _11000052 : NpcScript {
    internal _11000052(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000220$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407000222$ 
                // - $MyPCName$, do you know what the pride of $map:63000001$ is?
                switch (selection) {
                    // $script:0831180407000223$
                    // - The lovely scenery?
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0831180407000224$
                    // - The good-natured people?
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000225$ 
                // - That's right. The air is clean, the water is pure, and there are plenty of unique plants and animals to see. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
                return true;
            case 22:
                // $script:0831180407000226$ 
                // - That's right. The people of this place take care of each other like their own family. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
                return true;
            default:
                return true;
        }
    }
}
