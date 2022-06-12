using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000984: Naria
/// </summary>
public class _11000984 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003392$
    // - So... bad time travel trip? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003394$
                // - I wasn't always so forgetful. On that note... where am I? I don't know what went wrong this time... 
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
