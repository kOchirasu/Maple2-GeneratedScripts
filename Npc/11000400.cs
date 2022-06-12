using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000400: Newton
/// </summary>
public class _11000400 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001619$
    // - How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001621$
                // - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now?
                return -1;
            case (30, 0):
                // $script:0831180407001622$
                // - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
