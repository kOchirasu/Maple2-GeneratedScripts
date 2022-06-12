using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003471: 
/// </summary>
public class _11003471 : NpcScript {
    protected override int First() {
    }

    // Select 0:
    // $script:0817152010001894$
    // - Greetings.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (31, 0):
                // functionID=1 
                // $script:0817152010001901$
                // - No problem, no problem! I'll send it to you right away. Have a great time!
                return -1;
            case (32, 0):
                // functionID=1 
                // $script:0817152010001902$
                // - Looking for some fun at $map:02000405$? Then off you go!
                return -1;
            case (33, 0):
                // functionID=1 
                // $script:0817152010001903$
                // - I give you all these things because I care so dang much!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
