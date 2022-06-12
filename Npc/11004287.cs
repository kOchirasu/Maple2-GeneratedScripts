using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004287: Alberto Bean
/// </summary>
public class _11004287 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220212507014570$
    // - Nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220212507014571$
                // - You just might be up to the Queen Bean Rumble.
                return 10;
            case (10, 1):
                // $script:0220212507014572$
                // - I do think you shall be an amusement for Her Highness.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
