using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000980: Beefy
/// </summary>
public class _11000980 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003387$
    // - Nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003390$
                // - Got a spare umbrella?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
