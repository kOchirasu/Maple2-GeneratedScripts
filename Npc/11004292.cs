using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004292: Stuki
/// </summary>
public class _11004292 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011360$
    // - Welcome, welcome, to Mon Bloody Chouchou Hotel!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011363$
                // - Do you have a thirst for adventure? Then come to the Mon Bloody Chouchou Hotel and celebrate Halloween with us!
                switch (selection) {
                    // $script:1002141907011364$
                    // - Sounds fun!
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011365$
                // - Please take the portal here to the $map:63000065$. And enjoy your stay... Mwahahaha! 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
