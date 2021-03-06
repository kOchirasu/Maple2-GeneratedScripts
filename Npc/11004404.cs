using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004404: Oska
/// </summary>
public class _11004404 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011825$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011826$
                // - Worry not. The Green Hoods watch over this place.
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
