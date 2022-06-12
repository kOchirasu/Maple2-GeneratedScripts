using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004038: Ishura
/// </summary>
public class _11004038 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010061$
    // - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010062$
                // - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
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
