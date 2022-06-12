using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000052: Varlos
/// </summary>
public class _11000052 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000220$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000222$
                // - $MyPCName$, do you know what the pride of $map:63000001$ is?
                switch (selection) {
                    // $script:0831180407000223$
                    // - The lovely scenery?
                    case 0:
                        return 21;
                    // $script:0831180407000224$
                    // - The good-natured people?
                    case 1:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000225$
                // - That's right. The air is clean, the water is pure, and there are plenty of unique plants and animals to see. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
                return -1;
            case (22, 0):
                // $script:0831180407000226$
                // - That's right. The people of this place take care of each other like their own family. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
