using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004497: Axelrodi
/// </summary>
public class _11004497 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012376$
    // - I'm part of the team researching the fish of Kritias.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012377$
                // - I'm part of the team researching the fish of Kritias.
                return 10;
            case (10, 1):
                // $script:1227192907012378$
                // - The water here is highly toxic. Just a sip would tombstone an ordinary person. But see in there? Fish.
                switch (selection) {
                    // $script:1227192907012379$
                    // - How is that possible?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012380$
                // - I can't say anything conclusively just yet, but I think the aetherine in their bodies somehow protects them from the poison.
                return 11;
            case (11, 1):
                // $script:1227192907012381$
                // - Did the fish here evolve to use the aetherine to neutralize the poison?
                switch (selection) {
                    // $script:0114163707012717$
                    // - That's pretty handy.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114163707012718$
                // - Well, it's just a theory.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
