using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000260: Leo
/// </summary>
public class _11000260 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001072$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001074$
                // - I hope we nab $npcName:11000064[gender:0]$. He's caused so many people so much pain.
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
