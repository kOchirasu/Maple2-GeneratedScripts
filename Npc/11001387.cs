using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001387: Krata
/// </summary>
public class _11001387 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217193307005387$
    // - I'm tired. Really tired!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1223165107005549$
                // - I've been getting terrible joint pain lately. Normally that'd mean there's a storm brewing, but it doesn't rain here. Very strange.
                return 40;
            case (40, 1):
                // $script:1223165107005550$
                // - There's a rumor that all the ailments that have struck the town lately are from an ancient curse.
                switch (selection) {
                    // $script:1223165107005551$
                    // - What kind of curse?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1223165107005552$
                // - Never mind. I shouldn't have mentioned it to an outsider in the first place. If you'll excuse me, I need to gather herbs for my arthritis.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
