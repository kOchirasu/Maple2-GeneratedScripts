using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001194: Hicut
/// </summary>
public class _11001194 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1016202007004188$
    // - Sigh...
    //   I want to go home...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1016202007004191$
                // - This is no good. I can't get a good shot!
                //   What should I do? 
                switch (selection) {
                    // $script:1016202007004192$
                    // - What's wrong?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1016202007004193$
                // - It's may be bright out here, but our cameras our set up inside that cave, where it's much darker. I doubt we can get any usable footage as it stands.
                //   I should've brought $npcName:11001193[gender:1]$, my supervisor... 
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
