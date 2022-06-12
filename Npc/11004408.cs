using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004408: Veliche
/// </summary>
public class _11004408 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011833$
    // - The future is in our hands.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011834$
                // - Especially at times like these, we must maintain our composure.
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
