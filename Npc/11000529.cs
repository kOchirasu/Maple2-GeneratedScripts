using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000529: Blackeye
/// </summary>
public class _11000529 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407002267$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002270$
                // - Dark Wind has changed too much. Now it's crushing the citizens under authoritarian rule instead of protecting them like they used to. I can't let this continue.
                return -1;
            case (40, 0):
                // $script:0831180407002271$
                // - $MyPCName$, do the people in this city look happy to you?
                switch (selection) {
                    // $script:0831180407002272$
                    // - Yep!
                    case 0:
                        return 41;
                    // $script:0831180407002273$
                    // - Beats me.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002274$
                // - Then you're a fool. There's no point in discussing this further. Leave.
                return -1;
            case (42, 0):
                // $script:0831180407002275$
                // - Try to see through their deceptions. It's not hard to find the rotting heart of this city.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
