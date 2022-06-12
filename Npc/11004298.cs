using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004298: Ghost
/// </summary>
public class _11004298 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011381$
    // - Clean clean clean... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011384$
                // - It's my job to keep this hotel clean, and I'm darn good at it! Except... there's this one thing I can't seem to tidy up!
                switch (selection) {
                    // $script:1002141907011385$
                    // - What might that be?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011386$
                // - Over there, in the sofa by the window. There are papers stuck in there that I can't seem to get loose. Did someone put those there on purpose? 
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
