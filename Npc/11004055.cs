using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004055: Oska
/// </summary>
public class _11004055 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0614185307010083$
    // - The siege on Madrakan was successful, but it cost us a great deal.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0614185307010084$
                // - The siege on Madrakan was successful, but it cost us a great deal.
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
