using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003527: Pyrros Fard
/// </summary>
public class _11003527 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0816160115009051$
    // - Grrr...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009052$
                // - Grrr...
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
