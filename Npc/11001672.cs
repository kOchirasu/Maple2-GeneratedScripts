using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001672: Junta
/// </summary>
public class _11001672 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0711210007006722$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006893$
                // - They've pushed us all the way back to $map:63000029$...
                switch (selection) {
                    // $script:0727223007006894$
                    // - What's our next move?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006895$
                // - I thought we could handle this on our own, but there are too many of them. We have no choice but to report the situation to the master. He will know what to do.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
