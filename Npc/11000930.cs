using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000930: Mocamoca
/// </summary>
public class _11000930 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003302$
    // - I don't trust you humans. Caw!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003304$
                // - Humans are bad. Caw!
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
