using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001349: Zobek
/// </summary>
public class _11001349 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005309$
    // - What can I do for you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005312$
                // - Why would Mademoiselle Rue want to go into business with Cathy Catalina? They're polar opposites of each other. There's no way this partnership will last!
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
