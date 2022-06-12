using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000959: Darren
/// </summary>
public class _11000959 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003322$
    // - Step back. You stand around gawking like that and you're sure to get eaten.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003324$
                // - It's hard enough to keep black market dealers from slipping in from $map:02000100$. Now we have to deal with these stupid monsters!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
