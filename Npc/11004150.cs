using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004150: Harry
/// </summary>
public class _11004150 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010571$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010572$
                // - Are you here to participate in Mushking Royale too? I'm afraid we've already got a squad of four. I'll see you on the battlefield!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
