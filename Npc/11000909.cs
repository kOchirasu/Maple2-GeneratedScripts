using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000909: Liberation Army Orders
/// </summary>
public class _11000909 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407003269$
    // - If you can read this directive, follow the instructions in secret.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407003270$
                // - Access denied. Unauthorized personnel.
                return -1;
            case (20, 0):
                // $script:0831180407003271$
                // - Unauthorized personnel cannot view this directive.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
