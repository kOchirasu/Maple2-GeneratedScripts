using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001724: Mystery Person
/// </summary>
public class _11001724 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006974$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0804173107007076$
                // - Tell me what you have to say.
                switch (selection) {
                    // $script:0804173107007077$
                    // - Who are those two behind you?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0804173107007078$
                // - These are my companions. Don't worry, they aren't nearly as violent or nasty as they look. 
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
