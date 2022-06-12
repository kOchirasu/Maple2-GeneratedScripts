using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003414: Hero's Tomb
/// </summary>
public class _11003414 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0623153207008575$
    // - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0623180607008577$
                // - <i>Here lies Sharp Claw, the war chief who rebuilt $map:02000051$. His kind heart and dedicated work uplifted our people during our time of need, and for that he will always be remembered.</i>
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
