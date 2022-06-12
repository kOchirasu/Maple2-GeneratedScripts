using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003148: Einos
/// </summary>
public class _11003148 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0324141007008127$
    // - Did you remember your books?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0324141007008128$
                // - Of course you didn't. I don't know what I expected.
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
