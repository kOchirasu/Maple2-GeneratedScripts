using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003268: Ladin
/// </summary>
public class _11003268 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008218$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008219$
                // - After the Blue Lapenta broke, top scholars from across the world descended on $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
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
