using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004085: Oath Marker
/// </summary>
public class _11004085 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010290$
    // - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010291$
                // - <font color="#909090">(This enchanted marker has been warded against the ages. Ancient writing has been etched into it.)</font>
                return 10;
            case (10, 1):
                // $script:0622133907010292$
                // - <i>When our world was young, the goddess of light faded away. It became the responsibility of us fairfolk to carry what remained of her work into the future.</i>
                return 10;
            case (10, 2):
                // $script:0622133907010293$
                // - <i>The taint of the darkness remained. Without our goddess, it fell to us to seal it away.</i>
                return 10;
            case (10, 3):
                // $script:0622133907010294$
                // - <i>Someday, we believe that our goddess will return to us in mortal form. Until then, we wait and stand watch against the shadows.</i>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
