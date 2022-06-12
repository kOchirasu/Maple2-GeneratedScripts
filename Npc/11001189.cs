using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001189: Wei Hong
/// </summary>
public class _11001189 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1015162707004153$
    // - Betrayal is the quickest path to death.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1015162707004156$
                // - So what, they stole one of our trains? Quit whining.
                //   I haven't survived the criminal underworld this long by panicking every time someone came after me!
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
